import { Injectable } from '@angular/core';
import { ActivatedRouteSnapshot, CanActivate, Resolve, RouterStateSnapshot, UrlTree } from '@angular/router';
import { Observable } from 'rxjs';
import { MyDataTable } from '../my-data';
import { MyDataService } from '../my-data.service';

@Injectable({
  providedIn: 'root'
})
export class MyDataGuard implements Resolve<MyDataTable[]> {
  
  constructor (private myDataService: MyDataService) {}
  
  resolve(route: ActivatedRouteSnapshot, state: RouterStateSnapshot): MyDataTable[] | Observable<MyDataTable[]> | Promise<MyDataTable[]> {
      return this.myDataService.getData();
  }
}
