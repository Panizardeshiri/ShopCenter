import { Injectable } from '@angular/core';

import { HttpClient, HttpErrorResponse } from "@angular/common/http"
import { BehaviorSubject, throwError } from 'rxjs';
import { catchError, map, take, tap } from 'rxjs/operators';
import { environment } from 'src/environments/environment';

@Injectable({
  providedIn: 'root'
})
export class AuthService {

  apiUrl              = environment.apiUrl
  requestResponseMessage =  new BehaviorSubject<string>('')
  userIsLoggedIn = new BehaviorSubject<boolean>(false)




  constructor(public http:HttpClient) {
      const refresh_token: any = localStorage.getItem("refresh_token")
      const access_token: any = localStorage.getItem("access_token")

      this.renewAccessToken(access_token, refresh_token)
      
   }




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
        if ( refresh_token && this.check_token_expire(refresh_token)){
          this.userIsLoggedIn.next(!!access_token)
          return false
        }



      } else {
        localStorage.removeItem('access_token')
        
        if (refresh_token){

          if (this.check_token_expire(refresh_token)){

            return true
          }else{
            return false
          }

        }

      }
  
    } else {

      //  here we need to refresh the access token if refresh token exists
      if (refresh_token){

        if (this.check_token_expire(refresh_token)){
          return true

        }else{
          localStorage.removeItem('refresh_token');
          localStorage.removeItem('user_email')
          return false
        }
      }else{
        
        localStorage.removeItem('user_email')
        return false
      }
    }
  }


  renewAccessToken(access_token:string, refresh_token:string){
    if (this.sendNeedToRefreshMessage(access_token, refresh_token)){

      return this.http.post(this.apiUrl + '/accounts/api-vi/refresh/',
      {
       refresh :refresh_token
     }).pipe(
       catchError(this.handleError),
       tap( (data:any) =>{
         localStorage.setItem('refresh_token', data['refresh'])
         localStorage.setItem('access_token', data['access'])
         this.userIsLoggedIn.next(true)
       }
       )
     )

    }

  }




  signUpService(username:string, password:string, password2:string) {
    return this.http.post(this.apiUrl +"/accounts/api-vi/register/", {
      phone: username,
      password: password, 
      password2: password2
    }).pipe(
        catchError(this.handleError),
        tap( (data:any)=> {
          localStorage.setItem('refresh_token', data['refresh_token'])
          localStorage.setItem('access_token', data['access_token'])
          localStorage.setItem('user_phone', username)
          this.userIsLoggedIn.next(true)
          }
        )
      
      )
  }


  logInService(phone:string, password:string){

    return this.http.post(this.apiUrl + "/accounts/api-vi/login/",{
      phone: phone,
      password: password
    }).pipe(
      catchError(this.handleError),
      tap( ((data:any)=>{
        console.log("____________________log in  ",data )
        this.userIsLoggedIn.next(true),
        localStorage.setItem('refresh_token', data['refresh'] ),
        localStorage.setItem('access_token', data['access'] ),
        localStorage.setItem('user_phone', phone )
        this.requestResponseMessage.next('successfully loged in')
      } ))
    )

  }

  logOutService(){
    return this.http.post(this.apiUrl+ "/accounts/api-vi/logout/",{}).pipe( 
      catchError(this.handleError),
      tap( data=>{
        console.log("____________________log out  ",data )
        localStorage.removeItem('refresh_token')
        localStorage.removeItem('access_token')
        localStorage.removeItem('user_phone')
      } )
    )
  }


  resendVerificationEmail (email: string) {
    return this.http.post(this.apiUrl + "/accounts/api-vi/resend-code/", {
      email: email,
    }).pipe(
      catchError(this.handleError),
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
    if (errorRes.error['password1']){
      errorMessage=errorRes.error['password1']
    }
    if (errorRes.error['detail']){
      errorMessage=errorRes.error['detail']
    }else{
      return throwError(errorMessage)
    }
    return throwError(errorMessage)
  }




}
