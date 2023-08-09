import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HomeModule } from './home/home.module';
import { HeaderModule } from './header/header.module';
import { FooterModule } from './footer/footer.module';
import { NbThemeModule , NbSidebarModule, NbLayoutModule, NbButtonModule } from '@nebular/theme';
import { SideBarModule } from './side-bar/side-bar.module'
import {MatIconModule} from '@angular/material/icon';
import { AuthUserModule } from './auth-user/auth-user.module'

@NgModule({
  declarations: [
    AppComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    // import nebular module to here
    [    NbThemeModule.forRoot(),
    NbLayoutModule,
    NbSidebarModule.forRoot(),
    NbButtonModule,
  ],

  // import material module here
  [
    MatIconModule
  ],


    HomeModule,
    HeaderModule,
    FooterModule,
    SideBarModule,
    AuthUserModule,
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
