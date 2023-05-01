import { Component, ViewChild, ViewContainerRef, AfterViewInit, ElementRef, OnInit, Optional, Inject } from '@angular/core';
import { LoggerService } from './logger.service';
import { RoomsComponent } from './rooms/rooms.component';
import { localStorageToken } from './localstorage.token';
import { InitService } from './init.service';
import { ConfigService } from './services/config.service';
import { NavigationEnd, NavigationStart, Router } from '@angular/router';
import { filter } from 'rxjs';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent implements OnInit {
  title = 'hotelinventoryapp';

  // role = 'Admin';

  constructor(@Optional() private loggerService: LoggerService,
  @Inject(localStorageToken) private localStorage: any,
  private initService: InitService,
  private configService: ConfigService,
  private router: Router
  ) {
    console.log(initService.config);
  }

  @ViewChild('name', { static: true }) name!: ElementRef;

  ngOnInit() {
    // this.router.events.subscribe((event) => {
    //   console.log(event);
    // });

    this.router.events.pipe(
      filter((event) => event instanceof NavigationStart)
    ).subscribe((event) => {
      console.log('Navigation Started');
    });

    this.router.events.pipe(
      filter((event) => event instanceof NavigationEnd)
    ).subscribe((event) => {
      console.log('Navigation Completed');
    });

    this.loggerService?.Log('AppComponent.ngOnInit()');

    this.localStorage.setItem('name', 'Happy Hotel');
  }

  // @ViewChild('user', {read: ViewContainerRef}) vcr!: ViewContainerRef;

  ngAfterViewInit() {
    // const componentRef = this.vcr.createComponent(RoomsComponent);
    // componentRef.instance.numberOfRooms = 50;
  }
}
