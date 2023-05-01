import { Component, OnInit } from '@angular/core';
import { FormGroup, FormBuilder, FormControl, FormArray, Validators } from '@angular/forms';
import { ActivatedRoute } from '@angular/router';
import { exhaustMap, mergeMap, switchMap } from 'rxjs';
import { ConfigService } from '../services/config.service';
import { BookingService } from './booking.service';
import { CustomValidator } from './validators/custom-validator';

@Component({
  selector: 'app-booking',
  templateUrl: './booking.component.html',
  styleUrls: ['./booking.component.scss']
})
export class BookingComponent implements OnInit {

  bookingForm!: FormGroup;
  currentDate = new Date();

  get guests() {
    return this.bookingForm.get('guests') as FormArray;
  }

  constructor(private configService: ConfigService, private fb: FormBuilder, private bookingService: BookingService, private route: ActivatedRoute) { }

  ngOnInit(): void {
    const roomId = this.route.snapshot.paramMap.get('roomid');
    this.currentDate.setDate(this.currentDate.getDate());
    this.bookingForm = this.fb.group({
      roomID: new FormControl({ value: roomId, disabled: true }, { validators: [Validators.required]}),
      guestEmail: new FormControl('', {updateOn: 'blur', validators: [Validators.required, Validators.email]}),
      checkinDate: new FormControl(''),
      checkoutDate: new FormControl(''),
      bookingStatus: new FormControl(''),
      bookingAmount: new FormControl(''),
      bookingDate: new FormControl(this.currentDate),
      mobileNumber: new FormControl(''),
      guestName: new FormControl('', [Validators.required, Validators.minLength(5), CustomValidator.ValidateName, CustomValidator.ValidateSpecialChar('*')]),
      address: this.fb.group({
        addressLine1: new FormControl('', { validators: [Validators.required] }),
        addressLine2: new FormControl(''),
        city: new FormControl('', { validators: [Validators.required] }),
        state: new FormControl('', { validators: [Validators.required] }),
        country: new FormControl(''),
        zipCode: new FormControl(''),
      }),
      guests: this.fb.array([this.addGuestControl()]),
      tnc: new FormControl(false, {validators: [Validators.requiredTrue]})
    }, {updateOne: 'blur', validators: [CustomValidator.ValidateDate]});

    this.getBookingData();

    // this.bookingForm.valueChanges.subscribe((data) => {
    //   this.bookingService.bookRoom(data).subscribe((data) => {})
    // });

    // this.bookingForm.valueChanges.pipe(
    //   exhaustMap((data) => this.bookingService.bookRoom(data))
    // ).subscribe((data) => console.log(data))
  }

  getBookingData() {
    this.bookingForm.patchValue({
      guestEmail: '',
      checkinDate: '',
      checkoutDate: '',
      bookingStatus: '',
      bookingAmount: '',
      bookingDate: this.currentDate,
      mobileNumber: '',
      guestName: '',
      address: {
        addressLine1: '',
        addressLine2: '',
        city: '',
        state: '',
        country: '',
        zipCode: '',
      },
      guests: [],
      tnc: false

    })
  }

  addBooking() {
    console.log(this.bookingForm.getRawValue());
    // this.bookingService.bookRoom(this.bookingForm.getRawValue()).subscribe((data) => { console.log(data) })
    this.bookingForm.reset({
      roomID: '2',
      guestEmail: '',
      checkinDate: '',
      checkoutDate: '',
      bookingStatus: '',
      bookingAmount: '',
      bookingDate: this.currentDate,
      mobileNumber: '',
      guestName: '',
      address: {
        addressLine1: '',
        addressLine2: '',
        city: '',
        state: '',
        country: '',
        zipCode: '',
      },
      guests: [],
      tnc: false
    });
  }

  addGuest() {
    this.guests.push(
      this.addGuestControl()
    );
  }

  addGuestControl() {
    return this.fb.group({
      guestName: new FormControl('', { validators: [Validators.required] }),
      guestAge: new FormControl('')
    })
  }

  removeGuest(i: number) {
    this.guests.removeAt(i);
  }

  addPassport() {
    this.bookingForm.addControl('passport', new FormControl(''));
  }

  removePassport() {
    this.bookingForm.removeControl('passport');
  }

}

