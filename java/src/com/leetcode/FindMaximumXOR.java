package com.leetcode;

import java.util.Arrays;
import java.util.Stack;

/**
 * @author abhishekuppe
 */

class TrieNode {
    TrieNode[] children;
    int actualValue;

    public TrieNode() {
        this.children = new TrieNode[2];
        actualValue = -1;
    }
}

class Trie {
    TrieNode root;

    Trie() {
        root = new TrieNode();
    }

    void insert(Stack<Boolean> stack, int actualValue) {
        TrieNode temp = root;
        while (stack.size() > 0) {
            int val = stack.pop() ? 1 : 0;
            if (temp.children[val] == null) {
                temp.children[val] = new TrieNode();
            }
            temp = temp.children[val];
        }
        temp.actualValue = actualValue;
    }

    int searchMaximum() {
        TrieNode temp1 = root;
        TrieNode temp2 = root;

        return -1;
    }
}

public class FindMaximumXOR {

    public static void main(String[] args) {
        FindMaximumXOR findMaximumXOR = new FindMaximumXOR();
        findMaximumXOR.findMaximumXOR(new int[]{3, 10, 5, 25, 2, 8});
    }

    public int findMaximumXOR(int[] nums) {
        Trie trie = new Trie();

        int max = Arrays.stream(nums).reduce((a, b) -> Math.max(a, b)).getAsInt();

        int bits = 0;

        while (max > 0) {
            max = max >> 1;
            bits += 1;
        }

        for (int num : nums) {
            int temp = num;
            Stack<Boolean> stack = new Stack<>();

            while (num > 0) {
                stack.push((num & 1) == 1);
                num = num >> 1;
            }

            while (stack.size() < bits) {
                stack.push(false);
            }

            trie.insert(stack, temp);
        }

        return trie.searchMaximum();
    }
}
