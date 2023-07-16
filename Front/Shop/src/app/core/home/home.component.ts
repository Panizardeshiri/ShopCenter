import { Component, OnInit } from '@angular/core';
// import {ProductService} from 'src/app/services/product.service'
import {HttpClient, HttpErrorResponse} from "@angular/common/http"
@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {
   data : any
  // public noData: any;
  // public results = [];
  // productlisterror = ''

  // constructor(public productService:ProductService) {}
  constructor(private http:HttpClient) {}

  ngOnInit(): void {
    this.http.get<any>('http://127.0.0.1:8000/products/api-vi/products-list').subscribe(data=>{
      // console.log(data)
      this.data = data
      console.log(JSON.stringify(this.data))
    })}
      
           
  }

  // productslist(){
  //   this.productService.productlistService().subscribe((results)=>{
      
  //     this.data= results.results
  //     console.log('JSON Response = ', JSON.stringify(results))
      
  //   }, err => {
  //       console.log('*******************', err)
  //       this.productlisterror = err
  //   })
  // }




