package com.leetcode;

import java.util.ArrayList;
import java.util.List;

/**
 * @author abhishekuppe
 */
public class AllElementsInTwoBinarySearchTrees {

    public void inorder(TreeNode root, ArrayList<Integer> arrayList) {
        if (root == null) {
            return;
        }

        inorder(root.left, arrayList);
        arrayList.add(root.val);
        inorder(root.right, arrayList);
    }

    public List<Integer> getAllElements(TreeNode root1, TreeNode root2) {
        ArrayList<Integer> arrayList1 = new ArrayList<>();
        ArrayList<Integer> arrayList2 = new ArrayList<>();

        inorder(root1, arrayList1);
        inorder(root2, arrayList2);

        int i = 0, j = 0;

        ArrayList<Integer> result = new ArrayList<>();

        while (i < arrayList1.size() && j < arrayList2.size()) {
            if (arrayList1.get(i) < arrayList2.get(j)) {
                result.add(arrayList1.get(i++));
            } else {
                result.add(arrayList2.get(j++));
            }
        }

        while (i < arrayList1.size()) {
            result.add(arrayList1.get(i++));
        }

        while (j < arrayList2.size()) {
            result.add(arrayList2.get(j++));
        }

        return result;
    }
}
