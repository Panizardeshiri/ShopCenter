import { Component, OnInit } from '@angular/core';
import { AuthService } from '../services/auth.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})
export class HomeComponent implements OnInit {

  userIsLoggedIn :boolean;
  userSignedUp: boolean;
  loadingSpinner = false;
  resendMessage :string;
  loginMessage:string

  constructor(private authService: AuthService) { }

  ngOnInit(): void {
    
    // after that user signed up the message will shown to user
    this.authService.userIsLoggedIn.subscribe( data =>{
      if (data == true){
        this.userIsLoggedIn = true
        this.loginMessage = 'logged in successfully'
        setTimeout( ()=>{
          this.loginMessage = ''
        } , 3000)
        
      }
    })

    this.authService.userSignedUp.subscribe(data => {
      this.userSignedUp = data
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
