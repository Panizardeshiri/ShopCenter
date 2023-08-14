import { Injectable } from '@angular/core';
import { HttpClient, HttpErrorResponse } from "@angular/common/http"
import { BehaviorSubject, throwError } from 'rxjs';
import { catchError, map, take, tap } from 'rxjs/operators';
import { environment } from 'src/environments/environment';

@Injectable({
  providedIn: 'root'
})
export class AuthUserService {
  apiUrl              = environment.apiUrl 

  constructor(private http:HttpClient) { }

  signUpService(username:string, password:string, password2:string) {
    return this.http.post(this.apiUrl + "/accounts/api-vi/register/", {
      phone: username,
      password: password, 
      password2: password2
    }).pipe(
        catchError(this.handleError),
        tap( (data:any)=> {
          localStorage.setItem('refresh_token', data['refresh_token'])
          localStorage.setItem('access_token', data['access_token'])
          localStorage.setItem('user_email', username)
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
    if(errorRes.error.username){
      errorMessage=errorRes.error['username']
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
