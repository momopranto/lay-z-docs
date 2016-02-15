#include <iostream>
#include <vector>
#include <cstdlib>
using namespace std;

class Timer {
public:
    Timer() : start(clock()) {}
    double elapsed() { return ( clock() - start ) / CLOCKS_PER_SEC; }
    void reset() { start = clock(); }
private:
    double start;
};

void fillRandVector(vector<int>& vec, int size) {
  for (size_t i=0; i<size; ++i) {
    vec.push_back((rand() % 2001) - 1000);
  }
}

int maxSubSum1( const vector<int> & a )
{
    int maxSum = 0;
    for( int i = 0; i < a.size( ); ++i )
        for( int j = i; j < a.size( ); ++j )
        {
            int thisSum = 0;
            for( int k = i; k <= j; ++k )
                thisSum += a[ k ];

            if( thisSum > maxSum )
                maxSum   = thisSum;
        }
    return maxSum;
}

int maxSubSum2( const vector<int> & a )
{
    int maxSum = 0;

    for( int i = 0; i < a.size( ); ++i )
    {
        int thisSum = 0;
        for( int j = i; j < a.size( ); ++j )
        {
            thisSum += a[ j ];

            if( thisSum > maxSum )
                maxSum = thisSum;
        }
    }

    return maxSum;
}

int maxSubSum4( const vector<int> & a )
{
    int maxSum = 0, thisSum = 0;

    for( int j = 0; j < a.size( ); ++j )
    {
        thisSum += a[ j ];

        if( thisSum > maxSum )
            maxSum = thisSum;
        else if( thisSum < 0 )
            thisSum = 0;
    }

    return maxSum;
}

int vecAvg(const vector<int>& vec) {
  int sum;
  for (const int& n : vec) {
    sum += n;
  }
  return sum/vec.size();
}

int main() {
  cout.setf(ios::fixed, ios::floatfield);
  cout.precision(8);
  // cout << CLOCKS_PER_SEC << endl;
  // my clock per sec is 1000 (y)

  // Part 1: maxSubSum1
  vector<int> v1;
  Timer t;
  double nuClicks;
  // fillRandVector(v1, 128);
  // fillRandVector(v1, 256);
  // fillRandVector(v1, 512);
  // fillRandVector(v1, 1024);
  // fillRandVector(v1, 2048);
  fillRandVector(v1, 4096);
  t.reset();
  maxSubSum1(v1);
  nuClicks = t.elapsed();
  cout << "Calculated in " << nuClicks << " seconds" << endl;

  // Part 2: maxSubSum2
  vector<int> v2;
  Timer t2;
  double nuClicks2;
  // fillRandVector(v2, 128);
  // fillRandVector(v2, 256);
  // fillRandVector(v2, 512);
  // fillRandVector(v2, 1024);
  // fillRandVector(v2, 2048);
  fillRandVector(v2, 4096);
  t2.reset();
  maxSubSum2(v2);
  nuClicks2 = t2.elapsed();
  cout << "Calculated in " << nuClicks2 << " seconds" << endl;


  // Part 3: maxSubSum4
  vector<int> v3;
  Timer t3;
  double nuClicks3;
  // fillRandVector(v3, 128);
  // fillRandVector(v3, 256);
  // fillRandVector(v3, 512);
  // fillRandVector(v3, 1024);
  // fillRandVector(v3, 2048);
  fillRandVector(v3, 4096);
  t3.reset();
  maxSubSum4(v3);
  nuClicks3 = t3.elapsed();
  cout << "Calculated in " << nuClicks3 << " seconds" << endl  */

  Timer t5;
  vector<int> vals = {256, 512, 1024, 2048, 4096};
  for (int& n : vals) {
    // fragment 2a
    vector<int> vec2a;
    for (int i=0; i<1000; i++) {
      t5.reset();
      int sum = 0;
      for (int i = 0; i < n; i++)
        ++sum;
      vec2a.push_back(t5.elapsed());
    }
    cout << "Frag 2a Avg runtime for n as "<< n << ": " << vecAvg(vec2a) << endl;

    // fragment 2b
    vector<int> vec2b;
    for (int i=0; i<1000; i++) {
      t5.reset();
      int sum = 0;
      for(int i = 0; i < n; i++)
        for(int j = 0; j < n; ++j)
          ++sum;
      vec2b.push_back(t5.elapsed());
    }
    cout << "Frag 2b Avg runtime for n as "<< n << ": " << vecAvg(vec2a) << endl;


    // fragment 2c
    vector<int> vec2c;
    for (int i=0; i<1000; i++) {
      t5.reset();
      int sum = 0;
      for(int i = 0; i < n; i++)
        for(int j = 0; j < i; ++j)
          ++sum;
      vec2c.push_back(t5.elapsed());
    }
    cout << "Frag 2c Avg runtime for n as "<< n << ": " << vecAvg(vec2a) << endl;


    // fragment 2d
    vector<int> vec2d;
    for (int i=0; i<10; i++) {
      t5.reset();
      int sum = 0;
      for(int i = 0; i < n; i++)
        for(int j = 0; j < n; ++j)
          for(int k = 0; k < n; ++k)
            ++sum;
      vec2d.push_back(t5.elapsed());
    }
    cout << "Frag 2d Avg runtime for n as "<< n << ": " << vecAvg(vec2a) << endl;
}

  return 0;
}
