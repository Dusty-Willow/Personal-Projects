import { Component, EventEmitter, Input, OnChanges, OnInit, Output, SimpleChanges } from '@angular/core';

@Component({
  selector: 'app-pagination',
  templateUrl: './pagination.component.html',
  styleUrls: ['./pagination.component.scss']
})
export class PaginationComponent implements OnInit, OnChanges {
  @Input() currentPage: number = 1;
  @Input() entriesDisplayed: number = 5;
  @Input() totalEntries: number = 0;
  @Output() changePage = new EventEmitter<number>();
  
  pagesCount : number;
  pages : number[] = [];
  

  ngOnInit(): void {
    console.log("Bruh Base")
    console.log(this.totalEntries)

    this.pagesCount = Math.ceil(this.totalEntries / 5);
    this.pages = this.rangeOfPages(1, this.pagesCount);
    console.log(this.pages)
  }

  ngOnChanges(changes: SimpleChanges): void {
    this.pages = []
    this.pagesCount = Math.ceil(this.totalEntries / this.entriesDisplayed);
    this.pages = this.rangeOfPages(1, this.pagesCount);
  }

  rangeOfPages(start : number, end : number): number[] {
    return [...Array(end).keys()].map(element => element + start)
  }
}
