import { Component, Input, OnInit } from '@angular/core';
import { FormGroup, FormBuilder, Validators } from '@angular/forms';
import { AuthService } from '../services/auth.service';
import { NbDialogRef } from '@nebular/theme';


@Component({
  selector: 'app-auth-user',
  templateUrl: './auth-user.component.html',
  styleUrls: ['./auth-user.component.scss']
})
export class AuthUserComponent implements OnInit {

  constructor(private fb: FormBuilder,
            private authService: AuthService,
            protected dialogRef: NbDialogRef<any>, ) { }
  @Input() formStatus: string = '';
  signUpForm: FormGroup;
  loginForm : FormGroup;
  usernameValidator:any = Validators.pattern("^([0]{1}[0-9]{3}[0-9]{3}[0-9]{4})$|^([\+]{1}[0-9]{1,3}[0-9]{3}[0-9]{4,6})$");

  snippingLoading: boolean = false;

  requestMessage: string
  hasError :boolean = false

  ngOnInit(): void {


    this.signUpForm = this.fb.group({
      username: ['', [
        Validators.required,
        this.usernameValidator,
      ]],
      password:   ['', [Validators.required, Validators.minLength(8), Validators.pattern('^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[a-zA-Z]).{8,}$') ]],
      password1:  ['', [Validators.required, Validators.minLength(8)]],
    });

    this.loginForm = this.fb.group({

      username: ['', [
        Validators.required,
        this.usernameValidator,
      ]],
      password: ['', [Validators.required]],
    })
  }



  onSignUp(form:any){
    this.snippingLoading = true;
    const username = form.value.username
    const password = form.value.password
    const password1 = form.value.password1

    this.authService.signUpService(username, password, password1).subscribe( (data:any)=>{
            this.dialogRef.close()
    },errorMessage =>{
        this.requestMessage = errorMessage
        this.signUpForm.reset()
        this.snippingLoading = false
        this.hasError = true
        this.signUpForm.controls.username.setValue(username)
        this.signUpForm.controls.password.setValue(password)
        this.signUpForm.controls.password1.setValue(password)
    } )

    

  }


  onLogin(form:any){
    const username = form.value.username
    const password = form.value.password
    this.snippingLoading = true
    this.authService.logInService(username, password).subscribe( (data)=>{
      this.snippingLoading = false
      this.dialogRef.close()
    }, errorMessage =>{
      this.snippingLoading = false
      this.hasError = true
      this.requestMessage = errorMessage
      this.signUpForm.controls.username.setValue(username)
      this.signUpForm.controls.password.setValue(password)
      console.log("****************** login error ", errorMessage)
    }
    
    )
  }

  changeFormToSignIn(){
    this.formStatus = 'signIn'
   }

   changeFormToSignUp(){
    this.formStatus = 'signUp'
   }
}