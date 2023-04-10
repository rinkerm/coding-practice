using System.CodeDom.Compiler;
using System.Collections.Generic;
using System.Collections;
using System.ComponentModel;
using System.Diagnostics.CodeAnalysis;
using System.Globalization;
using System.IO;
using System.Linq;
using System.Reflection;
using System.Runtime.Serialization;
using System.Text.RegularExpressions;
using System.Text;
using System;

class Result
{

    /*
     * Complete the 'plusMinus' function below.
     *
     * The function accepts INTEGER_ARRAY arr as parameter.
     */

    public static void plusMinus(List<int> arr)
    {
            List<int> counts = new List<int>(){0,0,0};
            foreach(int num in arr)
            {
                if (num > 0)
                {
                    counts[0]+=1;
                }
                else if (num < 0)
                {
                    counts[1]+=1;
                }
                else
                {
                    counts[2]+=1;
                }
            }
            float pos = (float)counts[0]/arr.Count;
            float neg = (float)counts[1]/arr.Count;
            float zero = (float)counts[2]/arr.Count;
            Console.WriteLine(pos.ToString("0.000000"));
            Console.WriteLine(neg.ToString("0.000000"));
            Console.WriteLine(zero.ToString("0.000000"));
    }

}

class Solution
{
    public static void Main(string[] args)
    {
        int n = Convert.ToInt32(Console.ReadLine().Trim());

        List<int> arr = Console.ReadLine().TrimEnd().Split(' ').ToList().Select(arrTemp => Convert.ToInt32(arrTemp)).ToList();

        Result.plusMinus(arr);
    }
}

