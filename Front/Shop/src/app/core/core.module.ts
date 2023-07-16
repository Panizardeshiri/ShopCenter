import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { HeaderComponent } from './header/header.component';
import { HomeComponent } from './home/home.component';
import { FooterComponent } from './footer/footer.component';
import { SignupComponent } from './header/signup/signup.component';
import {MatDialogModule} from '@angular/material/dialog'; 
import { ReactiveFormsModule } from '@angular/forms';
import {MatIconModule} from '@angular/material/icon'



@NgModule({
  declarations: [
    HeaderComponent,
    HomeComponent,
    FooterComponent,
    SignupComponent
  ],
  imports: [
    CommonModule,
    MatDialogModule,
    ReactiveFormsModule,
    MatIconModule,
  ],
  exports: [
    HeaderComponent,
    HomeComponent,
    FooterComponent,
    SignupComponent
  ]
})
export class CoreModule { }
