import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { RoomsBookingComponent } from '../rooms-booking/rooms-booking.component';
import { RoomGuard } from './guards/room.guard';
import { RoomsAddComponent } from './rooms-add/rooms-add.component';
import { RoomsComponent } from './rooms.component';

const routes: Routes = [
  { path: '', component: RoomsComponent, canActivateChild: [RoomGuard], children: [
    { path: 'rooms/add', component: RoomsAddComponent },
    { path: ':id', component: RoomsBookingComponent }
  ] },
  // { path: 'rooms/add', component: RoomsAddComponent },
  // { path: 'rooms/:id', component: RoomsBookingComponent },

];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class RoomsRoutingModule { }
