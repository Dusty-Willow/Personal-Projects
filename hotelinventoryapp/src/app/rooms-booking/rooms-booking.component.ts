import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { map, Observable } from 'rxjs';

@Component({
  selector: 'app-rooms-booking',
  templateUrl: './rooms-booking.component.html',
  styleUrls: ['./rooms-booking.component.scss']
})
export class RoomsBookingComponent implements OnInit {

  id: number = 0;
  id$ = this.router.paramMap.pipe(map((params) => params.get('id')));

  constructor (private router: ActivatedRoute) {}

  ngOnInit(): void {
    // this.id = this.router.snapshot.params['id'];
    // this.router.params.subscribe((params) => {this.id = params['id']});
  }
}
