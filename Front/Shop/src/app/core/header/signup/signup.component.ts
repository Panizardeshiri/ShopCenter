import { Component, OnInit, OnChanges, SimpleChanges, OnDestroy, Input } from '@angular/core';
import { FormBuilder, FormGroup,Validators  } from '@angular/forms';
import {AuthService} from 'src/app/services/auth.service'
import { NbDialogRef, NbDialogService } from '@nebular/theme';
import { Router } from '@angular/router';
import { SignUpModel } from 'src/app/models/auth.model';
@Component({
  selector: 'app-signup',
  templateUrl: './signup.component.html',
  styleUrls: ['./signup.component.scss']
})
export class SignupComponent implements OnInit {
  

  constructor(public authService: AuthService,
              private fb: FormBuilder,
              private router: Router,
             )
    {}
  
    signUpForm: FormGroup;
  signupSuccess: string = ''
  snippingLoading: boolean = false
  signupError: string = ''
  loginError:string
  formStatus: string = 'signUp'
  showPasswordStatus: boolean = false;


  

  ngOnInit(): void {
    this.signUpForm = this.fb.group({
      phone: ['',[Validators.required,Validators.pattern("^([0]{1}[0-9]{3}[0-9]{3}[0-9]{4})|([\+]{1}[0-9]{1,3}[0-9]{3}[0-9]{4,6})")]],
      password: ['',[Validators.required, Validators.minLength(8), Validators.pattern('(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[$@$!%*?&])[A-Za-z0-9d$@$!%*?&].{8,150}')]],
      password2: ['',[Validators.required, Validators.minLength(8), Validators.pattern('(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[$@$!%*?&])[A-Za-z0-9d$@$!%*?&].{8,150}')]],
    });
  }
  onSignin(form: any) {
    this.snippingLoading = true;
    const phone = form.value.phone
    const password = form.value.password
    const password2 = form.value.password2

    
    this.authService.signUpService(phone, password, password2)
    .subscribe((data : SignUpModel) => {
      console.log(data)
      this.snippingLoading = false
      this.signupSuccess = data['message']
      
      this.router.navigate(['/'])
    }, err => {
      this.snippingLoading = false
      console.log('*******************', err)
      this.signupError = err
    }); 
    form.reset()   
    
   
  }
  OnPasswordToggle(){
    this.showPasswordStatus = !this.showPasswordStatus;
   }
   changeFormToSignIn(){
    this.formStatus = 'signIn'
   }

   changeFormToSignUp(){
    this.formStatus = 'signUp'
   }

}
