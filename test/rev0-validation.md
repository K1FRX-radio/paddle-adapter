# Rev 0 Validation

## Electrical

- [x] Tip-to-sleeve closure detected from left Begali paddle.
- [x] Ring-to-sleeve closure detected from right Begali paddle.
- [x] DIT and DAH operate independently.
- [x] Simultaneous closures are supported.
- [x] 10 ms software debounce removes observed contact chatter.

## USB desktop

- [x] KB2040 enumerates over USB.
- [x] DIT produces A key down/up.
- [x] DAH produces B key down/up.

## Browser compatibility

- [ ] K1FRX Morse Trainer test page shows live DIT press/release.
- [ ] K1FRX Morse Trainer test page shows live DAH press/release.
- [ ] Both paddles may be held simultaneously without losing state.
- [ ] Mapped keys do not enter unwanted text in the test page.

## Mobile

- [ ] Android phone recognizes adapter over USB-C.
- [ ] Browser receives key-down/key-up events.
- [ ] Both paddles operate independently.
- [ ] Assess latency and responsiveness.
- [ ] Confirm behavior when browser loses focus or phone sleeps.

## Exit criteria for Rev 0

Proceed to Rev A PCB architecture when:

1. Desktop browser behavior is reliable.
2. At least one target Android/browser combination works reliably.
3. We have enough evidence to choose the Rev A USB transport strategy.
