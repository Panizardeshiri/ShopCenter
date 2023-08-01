import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { HeaderComponent } from './header/header.component';
import { HomeComponent } from './home/home.component';
import { FooterComponent } from './footer/footer.component';
import { SignupComponent } from './header/signup/signup.component';
import {MatDialogModule} from '@angular/material/dialog'; 
import { ReactiveFormsModule } from '@angular/forms';
import {MatIconModule} from '@angular/material/icon';
import { SearchComponent } from './header/search/search.component';
import { ProductdetailComponent } from './home/productdetail/productdetail.component'
import { RouterModule, Routes } from '@angular/router';
import { FilterproductsPipe } from '../core/header/search/filterproducts.pipe';
import { FormsModule } from '@angular/forms';



@NgModule({
  declarations: [
    HeaderComponent,
    HomeComponent,
    FooterComponent,
    SignupComponent,
    SearchComponent,
    ProductdetailComponent,
    FilterproductsPipe
  ],
  imports: [
    CommonModule,
    MatDialogModule,
    ReactiveFormsModule,
    MatIconModule,
    RouterModule,
    FormsModule      
  ],
  exports: [
    HeaderComponent,
    HomeComponent,
    FooterComponent,
    SignupComponent
  ]
})
export class CoreModule { }
