import { Component, OnInit } from '@angular/core';
import {ActivatedRoute} from '@angular/router'
import {ProductService } from '../../../services/product.service'

@Component({
  selector: 'app-productdetail',
  templateUrl: './productdetail.component.html',
  styleUrls: ['./productdetail.component.css']
})
export class ProductdetailComponent implements OnInit {
  productdetail:any
  id :string

  constructor(private activatedRoute:ActivatedRoute , private productservic:ProductService ) { }

  ngOnInit(): void {
      this.productservic.sendIdToDetail.subscribe((data:any) =>{
        this.id = data
      })
      this.productservic.getProductbyid(this.id).subscribe((result)=>{
      this.productdetail = result
      console.log(result)

    })
  }

}
