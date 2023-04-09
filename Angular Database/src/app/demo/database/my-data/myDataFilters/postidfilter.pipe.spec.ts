import { postIdFilterPipe } from './postidfilter.pipe';

describe('postIdFilterPipe', () => {
    it('create an instance', () => {
      const pipe = new postIdFilterPipe();
      expect(pipe).toBeTruthy();
    });
  });