import { Component, Input, OnInit } from '@angular/core';
import { FormGroup, FormBuilder, Validators } from '@angular/forms';


@Component({
  selector: 'app-auth-user',
  templateUrl: './auth-user.component.html',
  styleUrls: ['./auth-user.component.scss']
})
export class AuthUserComponent implements OnInit {

  constructor(private fb: FormBuilder,) { }
  @Input() formStatus: string = '';
  signUpForm: FormGroup;
  loginForm : FormGroup;
  usernameValidator:any = Validators.pattern("^([0]{1}[0-9]{3}[0-9]{3}[0-9]{4})$|^([\+]{1}[0-9]{1,3}[0-9]{3}[0-9]{4,6})$");

  snippingLoading: boolean = false;

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

  }


  onLogin(form:any){
    const username = form.value.username
    const password = form.value.password
    this.snippingLoading = true
  }

  changeFormToSignIn(){
    this.formStatus = 'signIn'
   }

   changeFormToSignUp(){
    this.formStatus = 'signUp'
   }
}
