class Solution {
    public int[] nextGreaterElement(int[] nums1, int[] nums2) {
        Stack<Integer> stack = new Stack<>();
        HashMap<Integer, Integer> hashMap = new HashMap<>();
        for (int i = nums2.length - 1; i >= 0; i--) {
            int num = nums2[i];
            if (stack.isEmpty()) {
                stack.push(num);
                hashMap.put(num, -1);
            } else {
                if (num > stack.peek()) {
                    while (true) {
                        if (stack.isEmpty()) {
                            hashMap.put(num, -1);
                            break;
                        } else {
                            if (num < stack.peek()) {
                                hashMap.put(num, stack.peek());
                                break;
                            } else {
                                stack.pop();
                            }
                        }
                    }
                } else {
                    hashMap.put(num, stack.peek());
                }
                stack.push(num);
            }
        }

        int[] result = new int[nums1.length];
        for (int i = 0; i < nums1.length; i++) {
            result[i] = hashMap.get(nums1[i]);
        }

        return result;
    }
}