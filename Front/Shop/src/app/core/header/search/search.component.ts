import { Component, OnInit } from '@angular/core';
import {ActivatedRoute} from '@angular/router'
import {ProductService} from '../../../services/product.service'
import { product } from 'src/app/models/product.model';
import { FormBuilder } from '@angular/forms';
@Component({
  selector: 'app-search',
  templateUrl: './search.component.html',
  styleUrls: ['./search.component.css']
})
export class SearchComponent implements OnInit {
  result:any


 

  constructor(private activatedRoute:ActivatedRoute,private searchService:ProductService,private fb:FormBuilder) { }

  ngOnInit(): void {
    
    
    this.searchService.searchproductService().subscribe((response)=>{
      this.result = response

    })
  }
//     searchProduct(query:KeyboardEvent){
//       if(query){
//         const element = query.target as HTMLInputElement
//         console.warn(element.value)
//         this.searchService.searchproductService(element.value).subscribe((result)=>{
//         console.warn(result)})
  
//     }
// }
  








}
