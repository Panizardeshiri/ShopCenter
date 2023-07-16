import { Injectable, SimpleChanges } from '@angular/core';
import {HttpClient, HttpErrorResponse} from "@angular/common/http"
import {  BehaviorSubject, throwError } from 'rxjs';
import { catchError, map, take, tap } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  apiUrl ='http://127.0.0.1:8000/'
  userIsLoggedIn      = new BehaviorSubject<boolean>(false)
  signUpMessage       = new BehaviorSubject<string>('')
  needToRefreshToken  = new BehaviorSubject<boolean>(false)

  check_token_expire(token:string) {

    // JSON.parse convert string to json
    const jwt_data: any = JSON.parse( atob(token.split('.')[1]) )
    const now : number = Math.trunc( Date.now() / 1000 )

    if ( jwt_data.exp - now > 0 ){
      return true

    } else {
      return false

    }

  }

  sendNeedToRefreshMessage(access_token:any, refresh_token: any){

    if ( access_token){

      if (this.check_token_expire(access_token)){

        this.userIsLoggedIn.next(!!access_token)
        this.needToRefreshToken.next(false);

      } else {
        localStorage.removeItem('access_token')
        
        if (refresh_token){

          if (this.check_token_expire(refresh_token)){

            this.needToRefreshToken.next(true);
          }

        }

      }
  
    } else {

      //  here we need to refresh the access token if refresh token exists
      if (refresh_token){

        if (this.check_token_expire(refresh_token)){

          this.needToRefreshToken.next(true);
        }else{
          localStorage.removeItem('refresh_token');
          localStorage.removeItem('user_email')
          this.needToRefreshToken.next(false);
        }
      }else{
        localStorage.removeItem('user_email')
      }
    }


  }


  constructor(private http:HttpClient) { let refresh_token: string | null = localStorage.getItem('refresh_token')
  let access_token: any = localStorage.getItem('access_token');

  this.sendNeedToRefreshMessage(access_token, refresh_token)}

  signUpService(phone:string, password:string, password2:string) {
    return this.http.post(this.apiUrl + "accounts/api-vi/register/", {
      phone: phone,
      password: password, 
      password2: password2
    }).pipe(
        catchError(this.handleError),
        tap( (data:any)=> {
          localStorage.setItem('refresh_token', data['refresh_token'])
          localStorage.setItem('access_token', data['access_token'])
          localStorage.setItem('user_phone', phone)
          this.userIsLoggedIn.next(true)
          this.signUpMessage.next(data['message'])
          }
        )
      
      )
  }

  private handleError(errorRes:HttpErrorResponse){
    let errorMessage = 'an unknown error occurred'
    console.log('-----------',errorRes)
    if (!errorRes.error){
      return throwError(errorMessage)
    }
    if(errorRes.error.phone){
      errorMessage=errorRes.error['phone']
    }
    if(errorRes.error['password']){
      errorMessage=errorRes.error['password']
    }
    if (errorRes.error['password2']){
      errorMessage=errorRes.error['password2']
    }
    if (errorRes.error['detail']){
      errorMessage=errorRes.error['detail']
    }else{
      return throwError(errorMessage)
    }
    return throwError(errorMessage)
  }





}
