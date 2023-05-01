import { HttpEventType } from '@angular/common/http';
import { Component, DoCheck, OnInit, ViewChild, AfterViewInit, AfterViewChecked, OnDestroy } from '@angular/core';
import { FormControl } from '@angular/forms';
import { catchError, map, Observable, of, Subject, Subscription } from 'rxjs';
import { HeaderComponent } from '../header/header.component';
import { Room, RoomList } from './rooms';
import { RoomsService } from './services/rooms.service';

@Component({
  selector: 'app-rooms',
  templateUrl: './rooms.component.html',
  styleUrls: ['./rooms.component.scss']
})
export class RoomsComponent implements OnInit, DoCheck, AfterViewInit, AfterViewChecked {

  hotelName = 'The Happy Hotel';
  numberOfRooms = 10;
  hideRooms = true;

  rooms: Room = {
    totalRooms: 20,
    availableRooms: 10,
    bookedRooms: 5
  }

  roomList: RoomList[] = [];

  subscription!: Subscription;

  error$ = new Subject<string>();

  getError$ = this.error$.asObservable();

  rooms$ = this.roomsService.getRooms$.pipe(
    catchError((err) => {
      console.log(err);
      this.error$.next(err.message);
      return of([]);
    })
  );

  priceFilter = new FormControl(0);

  roomsCount$ = this.roomsService.getRooms$.pipe(
    map((rooms) => rooms.length)
  );

  stream = new Observable<string>(observer => {
    observer.next('user1');
    observer.next('user2');
    observer.next('user3');
    observer.complete();
  });

  @ViewChild(HeaderComponent) headerComponent!: HeaderComponent;

  selectedRoom!: RoomList;

  constructor(private roomsService: RoomsService) { }

  ngDoCheck(): void {
    // console.log("Bruh");
  }

  totalBytes = 0;

  ngOnInit(): void {

    this.roomsService.getPhotos().subscribe((event) => {
      switch (event.type) {
        case HttpEventType.Sent: {
          console.log('Request Made!');
          break;
        }
        case HttpEventType.ResponseHeader: {
          console.log('Request Success!');
          break;
        }
        case HttpEventType.DownloadProgress: {
          this.totalBytes += event.loaded;
          break;
        }
        case HttpEventType.Response: {
          console.log(event.body);
        }
      }
    });

    this.stream.subscribe((data) => console.log(data));
    // this.roomsService.getRooms$.subscribe(rooms => {
    //   this.roomList = rooms;
    // });
  }

  ngAfterViewInit(): void {
    this.headerComponent.title = "Welcome to The Happy Hotel";
  }

  ngAfterViewChecked() {

  }

  toggle() {
    this.hideRooms = !this.hideRooms;
  }

  selectRoom(room: RoomList) {
    this.selectedRoom = room;
  }

  addRoom() {
    const room: RoomList = {
      roomNumber: (this.roomList.length + 1).toString(),
      roomType: 'Basement',
      amenities: 'Air-Conditioner, Free Wi-Fi, Bathroom, Kitchen',
      price: 250,
      photos: 'https://media.istockphoto.com/id/1293762741/photo/modern-living-room-interior-3d-render.jpg?s=1024x1024&w=is&k=20&c=KJNOdrG3iN0AKdcQfg65atySC1HLFgbikY2DEAkJDPE=',
      checkinTime: new Date('22-March-2023'),
      checkoutTime: new Date('23-March-2023'),
      rating: 2.5
    };

    // this.roomList.push(room); // This statement does not adhere to immutability
    // this.roomList = [...this.roomList, room];
    this.roomsService.addRoom(room).subscribe((data) => {
      this.roomList = data;
    });
  }

  editRoom() {
    const room: RoomList = {
      roomNumber: '3',
      roomType: 'Basement',
      amenities: 'Air-Conditioner, Free Wi-Fi, Bathroom, Kitchen',
      price: 250,
      photos: 'https://media.istockphoto.com/id/1293762741/photo/modern-living-room-interior-3d-render.jpg?s=1024x1024&w=is&k=20&c=KJNOdrG3iN0AKdcQfg65atySC1HLFgbikY2DEAkJDPE=',
      checkinTime: new Date('22-March-2023'),
      checkoutTime: new Date('23-March-2023'),
      rating: 2.5
    };

    this.roomsService.editRoom(room).subscribe((data) => {
      this.roomList = data;
    });
  }

  deleteRoom() {
    this.roomsService.deleteRoom('3').subscribe((data) => {
      this.roomList = data;
    });
  }

  ngOnDestroy() {
    if (this.subscription) {
      this.subscription.unsubscribe();
    }
  }
}
