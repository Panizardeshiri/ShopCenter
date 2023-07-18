import { Component, OnInit } from '@angular/core';
import {ProductService} from 'src/app/services/product.service'
import {HttpClient, HttpErrorResponse} from "@angular/common/http"

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {
   Products : any
   productlisterror=''
 
   
 

  constructor(public productService:ProductService) {}
 
  ngOnInit(): void {
   
    this.productService.productlistService().subscribe(response=>{
      this.Products = response 
           
      console.log(JSON.stringify(this.Products))
    },err=>{
      this.productlisterror=err
    })

   
  
  }
 
  // filteredImages(value:any) {
  //   // const imageString = value.replace('http://127.0.0.1:8000/','http://localhost:4200/', '')
  //   const imageString = value.replace('http://localhost:4200/', '')

  //   return imageString
  //   }


           
  }

 



