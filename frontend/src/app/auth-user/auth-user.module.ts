import { NgModule, CUSTOM_ELEMENTS_SCHEMA  } from '@angular/core';
import { CommonModule } from '@angular/common';
import { AuthUserComponent } from './auth-user.component';
import { FormsModule, ReactiveFormsModule, } from '@angular/forms';
import { NbCardModule, NbFormFieldModule, NbInputModule, NbSpinnerModule } from '@nebular/theme';
import {MatIconModule} from '@angular/material/icon';
import { NbEvaIconsModule } from '@nebular/eva-icons';
import { NbIconModule } from '@nebular/theme';



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
      NbSpinnerModule,
      NbInputModule,
      NbEvaIconsModule,
      NbIconModule,
      NbFormFieldModule,
    ],

    // import material module here
    [
      MatIconModule,
    ],
  ],
  exports: [
    AuthUserComponent
  ],
  schemas: [ CUSTOM_ELEMENTS_SCHEMA],
})
export class AuthUserModule { }
