import { ComponentFixture, TestBed } from '@angular/core/testing';

import { MydatatableComponent } from './mydatatable.component';

describe('MydatatableComponent', () => {
  let component: MydatatableComponent;
  let fixture: ComponentFixture<MydatatableComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ MydatatableComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(MydatatableComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
