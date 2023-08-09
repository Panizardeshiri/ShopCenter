import { Component, OnInit } from '@angular/core';
import {Router} from '@angular/router'
import {MatDialog} from '@angular/material/dialog';
import { SignupComponent } from './signup/signup.component';
import {ProductService} from '../../services/product.service'
import {ActivatedRoute} from '@angular/router'
import {ProductdetailComponent} from '../home/productdetail/productdetail.component'

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.css']
})
export class HeaderComponent implements OnInit {
  result:any
  searchText: any;

  constructor(public dialog: MatDialog, private route:Router,private searchService:ProductService,private activatedRoute:ActivatedRoute ,public productService:ProductService) { }

  openDialog() {
    this.dialog.open(SignupComponent);
  }
  opencomponent() {
    this.dialog.open(ProductdetailComponent);
  }


  ngOnInit(): void {
   
   this.searchService.searchproductService().subscribe((response)=>{
      this.result = response

    })
  }
  getProducId(id:any){
    this.productService.sendIdToDetail.next(id)
  }

  submit(val:string){
    console.log(val)
    this.route.navigate([`search/${val}`])
  }

}
