import { Component, OnInit,Input } from '@angular/core';
import { FormBuilder, FormGroup,Validators  } from '@angular/forms';

@Component({
  selector: 'app-signup',
  templateUrl: './signup.component.html',
  styleUrls: ['./signup.component.css']
})
export class SignupComponent implements OnInit {
  

  constructor(private fb: FormBuilder) {}
  SignupForm: FormGroup;

  

  ngOnInit(): void {
    this.SignupForm = this.fb.group({
      phone: ['',[Validators.required,Validators.pattern("^([0]{1}[0-9]{3}[0-9]{3}[0-9]{4})|([\+]{1}[0-9]{1,3}[0-9]{3}[0-9]{4,6})")]],
      password: ['',[Validators.required, Validators.minLength(8), Validators.pattern('(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[$@$!%*?&])[A-Za-z0-9d$@$!%*?&].{8,150}')]],
    });
  }
  onSubmit(form: FormGroup) {
    console.log('Valid?',  form.valid); // true or false
    console.log('Phone',form.value.phone) ;
    console.log('Password',form.value.password);
   
  }

}
