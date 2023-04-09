import { ComponentFixture, TestBed } from '@angular/core/testing';

import { MyArchiveComponent } from './my-archive.component';

describe('MyArchiveComponent', () => {
  let component: MyArchiveComponent;
  let fixture: ComponentFixture<MyArchiveComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ MyArchiveComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(MyArchiveComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
