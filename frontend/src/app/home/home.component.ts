import { Component, OnInit } from '@angular/core';
import { AuthService } from '../services/auth.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})
export class HomeComponent implements OnInit {

  userIsLoggedIn :boolean;
  userIsSignUp: boolean;
  loadingSpinner = false;
  resendMessage :string;

  constructor(private authService: AuthService) { }

  ngOnInit(): void {
    
    // after that user signed up the message will shown to user
    this.authService.userIsLoggedIn.subscribe( data =>{
      if (data == true){
        this.userIsSignUp = true
      }
    })
  }


  onResendEmail(){
    this.loadingSpinner = true
    let email: any = localStorage.getItem('user_email')
    this.authService.resendVerificationEmail(email).subscribe( (data)=>{
      this.loadingSpinner = false;
      this.resendMessage = 'Email resend please check your email again!'
    }, (error)=>{
      this.loadingSpinner = false;
    })
  }

}
