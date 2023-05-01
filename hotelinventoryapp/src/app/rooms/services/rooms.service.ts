import { HttpClient, HttpHeaders, HttpRequest } from '@angular/common/http';
import { Inject, Injectable } from '@angular/core';
import { shareReplay } from 'rxjs';
import { AppConfig } from '../../AppConfig/appconfig.interface';
import { APP_SERVICE_CONFIG } from '../../AppConfig/appconfig.service';
import { RoomList } from '../rooms';

@Injectable({
  providedIn: 'root'
})
export class RoomsService {

  roomList: RoomList[] = [];

  header = new HttpHeaders({'token': '1234567890'});
  getRooms$ = this.http.get<RoomList[]>('/api/rooms').pipe(
    shareReplay(1)
  );

  constructor(@Inject(APP_SERVICE_CONFIG) private config: AppConfig, private http: HttpClient) {
    console.log(this.config.apiEndpoint);
  }

  getRooms() {
    return this.http.get<RoomList[]>('/api/rooms');
  }

  addRoom(room: RoomList) {
    return this.http.post<RoomList[]>('/api/rooms', room);
  }

  editRoom(room: RoomList) {
    return this.http.put<RoomList[]>(`/api/rooms/${room.roomNumber}`, room);
  }

  deleteRoom(id: string) {
    return this.http.delete<RoomList[]>(`/api/rooms/${id}`);
  }

  getPhotos() {
    const request = new HttpRequest('GET', `https://jsonplaceholder.typicode.com/photos`, 
    {
      reportProgress: true,
    });
    return this.http.request(request);
  }
}


    // {
    //   roomNumber: 1,
    //   roomType: 'Deluxe',
    //   amenities: 'Air-Conditioner, Free Wi-Fi, Bathroom, Kitchen',
    //   price: 1000,
    //   photos: 'https://media.istockphoto.com/id/1293762741/photo/modern-living-room-interior-3d-render.jpg?s=1024x1024&w=is&k=20&c=KJNOdrG3iN0AKdcQfg65atySC1HLFgbikY2DEAkJDPE=',
    //   checkinTime: new Date('22-March-2023'),
    //   checkoutTime: new Date('23-March-2023'),
    //   rating: 3.5
    // },
    // {
    //   roomNumber: 2,
    //   roomType: 'Luxury',
    //   amenities: 'Air-Conditioner, Free Wi-Fi, Bathroom, Kitchen',
    //   price: 1500,
    //   photos: 'https://media.istockphoto.com/id/1208205959/photo/beautiful-living-room-interior-with-hardwood-floors-and-and-view-of-kitchen-in-new-luxury-home.jpg?s=1024x1024&w=is&k=20&c=ymN09UbwY7_xFMHd1aNZyh9b5MiQV6Xp9VU_khSkB3M=',
    //   checkinTime: new Date('22-March-2023'),
    //   checkoutTime: new Date('23-March-2023'),
    //   rating: 4.2
    // },
    // {
    //   roomNumber: 3,
    //   roomType: 'Standard',
    //   amenities: 'Air-Conditioner, Free Wi-Fi, Bathroom, Kitchen',
    //   price: 500,
    //   photos: 'https://media.istockphoto.com/id/1271897890/photo/living-room-interior-in-loft-industrial-style.jpg?s=1024x1024&w=is&k=20&c=GkGIE7HnLk8UR8CeFwec_fviqGWXtrCcU-mjVovlPSo=',
    //   checkinTime: new Date('22-March-2023'),
    //   checkoutTime: new Date('23-March-2023'),
    //   rating: 4.6
    // }