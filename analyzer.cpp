#include <utility>
#include <iostream>

#include "StringData.h"

#define ll long long

int linear_search(const std::vector<std::string>& container, const std::string& element)
{
    for (size_t i = 0; i < container.size(); i++)
    {
        const std::string& current_elem = container[i];
        if (current_elem == element)
            return i;
    }
    return -1;
}

int binary_search(const std::vector<std::string>& container, const std::string& element)
{
    int lower = 0, upper = container.size() - 1, mid = 0;

    while (lower <= upper)
    {
        mid = lower + (upper - lower) /2;
        if (container[mid] < element)
            lower = mid + 1;
        else if (container[mid] > element)
            upper = mid - 1;
        else 
            return mid;
    }
    return -1;
}

template<typename T, typename... functionArgs, typename... inputArgs>
std::pair<T, ll> time_function(T (*func)(functionArgs...), inputArgs... args)
{
    ll start_time = systemTimeNanoseconds();
    T result = func(args...);
    ll end_time = systemTimeNanoseconds();
    return {result, end_time - start_time};
}

int main() 
{
    const std::vector<std::string> data = getStringData();
    const char* to_search[3] = {"not_here", "mzzzz", "aaaaa"};

    for (const auto* search_string : to_search)
    {
        auto [linear_index, linear_time] = time_function(linear_search, data, search_string);
        auto [binary_index, binary_time] = time_function(binary_search, data, search_string);
        printf("Searching for \"%s\"...\n", search_string);
        printf("Binary Index: %i\nBinary Time: %i ns\n", binary_index, binary_time);
        printf("Linear Index: %i\nLinear Time: %i ns\n\n", linear_index, linear_time);
    }
    
    return 0;
}