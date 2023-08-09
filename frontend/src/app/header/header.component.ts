import { Component, OnInit } from '@angular/core';
import { NbDialogService } from '@nebular/theme';
import { AuthUserComponent } from '../auth-user/auth-user.component';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.scss']
})
export class HeaderComponent implements OnInit {

  constructor(private dialogService: NbDialogService,) { }

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

  ngOnInit(): void {
  }

}
