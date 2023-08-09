import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { HeaderComponent } from './header.component';
import { MatToolbarModule } from '@angular/material/toolbar';
import { NbDialogModule } from '@nebular/theme';


@NgModule({
  declarations: [
    HeaderComponent
  ],
  imports: [
    CommonModule, 
    // import nebular module here
    [
      NbDialogModule.forRoot(),
    ],
    // import material module here
    [
      MatToolbarModule
    ], 
  ],
  exports: [
    HeaderComponent
  ]
})
export class HeaderModule { }
