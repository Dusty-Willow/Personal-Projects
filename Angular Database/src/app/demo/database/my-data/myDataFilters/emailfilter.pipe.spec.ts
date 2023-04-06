import { emailFilterPipe } from './emailfilter.pipe';

describe('emailFilterPipe', () => {
    it('create an instance', () => {
      const pipe = new emailFilterPipe();
      expect(pipe).toBeTruthy();
    });
  });