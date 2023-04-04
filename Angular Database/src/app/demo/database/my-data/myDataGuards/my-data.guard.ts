import { Injectable } from '@angular/core';
import { ActivatedRouteSnapshot, CanActivate, Resolve, RouterStateSnapshot, UrlTree } from '@angular/router';
import { Observable } from 'rxjs';
import { MyData } from '../my-data';
import { MyDataService } from '../my-data.service';

@Injectable({
  providedIn: 'root'
})
export class MyDataGuard implements Resolve<MyData[]> {
  
  constructor (private myDataService: MyDataService) {}
  
  resolve(route: ActivatedRouteSnapshot, state: RouterStateSnapshot): MyData[] | Observable<MyData[]> | Promise<MyData[]> {
      return this.myDataService.getData();
  }
}
