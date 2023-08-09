import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { AuthUserComponent } from './auth-user.component';
import { FormsModule, ReactiveFormsModule, } from '@angular/forms';
import { NbCardModule, NbSpinnerModule } from '@nebular/theme';
import {MatIconModule} from '@angular/material/icon';
// import { NbDialogModule } from '@nebular/theme';


@NgModule({
  declarations: [
    AuthUserComponent
  ],
  imports: [
    CommonModule,
    FormsModule,
    ReactiveFormsModule,
    NbCardModule,
    
    // import nebular module here
    [
      NbSpinnerModule
    ],

    // import material module here
    [
      MatIconModule,
    ],
  ],
  exports: [
    AuthUserComponent
  ]
})
export class AuthUserModule { }
