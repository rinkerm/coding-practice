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
     * Complete the 'timeConversion' function below.
     *
     * The function is expected to return a STRING.
     * The function accepts STRING s as parameter.
     */

    public static string timeConversion(string s)
    {
        int n = s.Length;
        if(s.Substring(n-2) == "AM")
        {
            int h = Int32.Parse(s.Substring(0,2));
            if(h == 12){h=h-12;}
            if(h < 10)
            {
                s = "0" + h + s.Substring(2,n-4);
            }
            else
            {
                s = h + s.Substring(2,n-4);
            }
        }
        else
        {
            int h = Int32.Parse(s.Substring(0,2));
            if(h != 12)
            {
                h+=12;
            }
            s = h + s.Substring(2,n-4);
        }
        return s;
    }
}

class Solution
{
    public static void Main(string[] args)
    {
        TextWriter textWriter = new StreamWriter(@System.Environment.GetEnvironmentVariable("OUTPUT_PATH"), true);

        string s = Console.ReadLine();

        string result = Result.timeConversion(s);

        textWriter.WriteLine(result);

        textWriter.Flush();
        textWriter.Close();
    }
}

