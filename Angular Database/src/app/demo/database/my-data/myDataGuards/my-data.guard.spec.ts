import { TestBed } from '@angular/core/testing';

import { MyDataGuard } from './my-data.guard';

describe('MyDataGuard', () => {
  let guard: MyDataGuard;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    guard = TestBed.inject(MyDataGuard);
  });

  it('should be created', () => {
    expect(guard).toBeTruthy();
  });
});
