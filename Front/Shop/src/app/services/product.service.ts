import { Injectable } from '@angular/core';
import {HttpClient, HttpErrorResponse} from "@angular/common/http"
import {  BehaviorSubject, throwError,Observable } from 'rxjs';
import { catchError, map, take, tap } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class ProductService {
  apiUrl ='http://127.0.0.1:8000/'
  productslist = new BehaviorSubject<string>('')

  constructor(private http:HttpClient) { }

  productlistService() {
    return this.http.get(this.apiUrl+'products/api-vi/products-list').pipe(
      catchError(this.handleError)
      
    
    )
  }

  private handleError(errorRes:HttpErrorResponse){
    let errorMessage = 'an unknown error occurred'
    console.log('-----------',errorRes)
    if (!errorRes.error){
      return throwError(errorMessage)
    }
    
    return throwError(errorMessage)
  }


}

