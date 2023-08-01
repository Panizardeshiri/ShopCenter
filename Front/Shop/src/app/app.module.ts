import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule} from '@angular/forms';
import { CommonModule } from '@angular/common'
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { CoreModule } from './core/core.module';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import {HttpClientModule, HTTP_INTERCEPTORS} from '@angular/common/http';
import { RouterModule, Routes } from '@angular/router';
import {HomeComponent} from 'src/app/core/home/home.component'
import { SearchComponent } from './core/header/search/search.component';
import {ProductdetailComponent} from '../app/core/home/productdetail/productdetail.component';
// import { FilterproductsPipe } from './core/header/search/filterproducts.pipe';
// import { Ng2SearchPipeModule } from 'ng2-search-filter'


const routes : Routes = [
  {path: '',component: HomeComponent},
  {path:'product-detail/:name',component: ProductdetailComponent},
  {path:'search/:query',component:SearchComponent}
  // {path:'search/:query',component:SearchComponent}
]





@NgModule({
  declarations: [
    AppComponent,
    
    
   
    
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    CoreModule,
    BrowserAnimationsModule,
    HttpClientModule,
    CommonModule,
    RouterModule.forRoot(routes),
    
  ],
  providers: [ ],
  bootstrap: [AppComponent]
})
export class AppModule { }
