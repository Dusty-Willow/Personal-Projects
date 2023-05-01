import { ChangeDetectionStrategy, Component, EventEmitter, Input, OnChanges, OnDestroy, OnInit, Output, SimpleChanges } from '@angular/core';
import { RoomList } from '../rooms';

@Component({
  selector: 'app-rooms-list',
  templateUrl: './rooms-list.component.html',
  styleUrls: ['./rooms-list.component.scss'],
  // changeDetection: ChangeDetectionStrategy.OnPush
})
export class RoomsListComponent implements OnInit, OnChanges, OnDestroy {

  @Input() rooms : RoomList[] = [];

  @Input() title : string = '';

  @Input() price : number | null = 999999;

  @Output() selectedRoom = new EventEmitter<RoomList>();

  constructor() {}

  ngOnDestroy(): void {
    console.log("OnDestroy Called.");
  }

  selectRoom(room: RoomList) {
    this.selectedRoom.emit(room);
  }

  ngOnInit(): void {
    
  }

  ngOnChanges(changes: SimpleChanges): void {
    console.log(changes);
  }

}
