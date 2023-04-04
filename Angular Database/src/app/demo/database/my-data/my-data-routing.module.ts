import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { MyDataComponent } from './my-data.component';
import { MyDataGuard } from './myDataGuards/my-data.guard';

const routes: Routes = [{ path: '', component: MyDataComponent, resolve: {myData: MyDataGuard} }];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class MyDataRoutingModule { }
