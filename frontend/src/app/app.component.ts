import { Component } from '@angular/core';
import { NbSidebarService } from '@nebular/theme';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {

  constructor(private sidebarService: NbSidebarService){}
  title = 'frontend';
  ExpandedSidebar = false;


  toggle() {
    this.sidebarService.toggle(true, 'left');
    this.ExpandedSidebar = !this.ExpandedSidebar;
  }


}
