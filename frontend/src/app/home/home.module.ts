import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { HomeComponent } from './home.component';
import { NbCardModule, NbSpinnerModule } from '@nebular/theme';
import {MatIconModule} from '@angular/material/icon';



@NgModule({
  declarations: [
    HomeComponent
  ],
  imports: [
    CommonModule, 

    // import nebular module here
    [
      NbSpinnerModule,
      NbCardModule
    ],

    // import material icon here
    [
      MatIconModule,
    ],

  ],
  exports: [
    HomeComponent
  ]
})
export class HomeModule { }
