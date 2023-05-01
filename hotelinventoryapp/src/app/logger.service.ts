import { Injectable } from '@angular/core';

@Injectable()
export class LoggerService {

  constructor() { }

  Log(msg: string) {
    console.log(msg);
  }
}
