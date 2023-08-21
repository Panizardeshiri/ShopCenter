import { Component, OnInit,OnChanges ,OnDestroy, SimpleChanges } from '@angular/core';
import { NbDialogService } from '@nebular/theme';
import { AuthUserComponent } from '../auth-user/auth-user.component';
import { AuthService } from '../services/auth.service';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.scss']
})
export class HeaderComponent implements OnInit {
  userPhoneNumber :any;
  signUpMessage :string;

  constructor(private dialogService: NbDialogService,
          private authService: AuthService) { }

  onSignUp() {
    const dialogRef = this.dialogService.open(AuthUserComponent, {    context: {
      formStatus: 'signUp',
    }, },);
  }

  onSignIn() {
    const dialogRef = this.dialogService.open(AuthUserComponent, {    context: {
      formStatus: 'signIn',
    }, },);
  }
  protected open(closeOnBackdropClick: boolean) {
    this.dialogService.open(AuthUserComponent, { closeOnBackdropClick ,context: 'pass data in template' },);
  } 

  onLogOut(){
    this.authService.logOutService().subscribe( data =>{
      this.authService.userIsLoggedIn.next(false)
      this.userPhoneNumber=''
    })
  }

  ngOnInit(): void {
      // after that user signed up sugnup and sign in message must change to phone number
      this.authService.userIsLoggedIn.subscribe(data=>{
        if (data==true){
            this.userPhoneNumber = localStorage.getItem('user_phone')
        }
      })

      this.authService.userSignedUp.subscribe(data=>{
        if (data==true){
            this.userPhoneNumber = localStorage.getItem('user_phone')
        }
      })



  }


  ngOnChanges(changes: SimpleChanges) {
    console.log(changes)
  }

}
