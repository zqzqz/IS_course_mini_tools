## environment
* docker version 1.13.1
* clone https://github.com/sunblaze-ucb/ekiden


## build the project
### status
```
./scripts/sgx-enter.sh
```
### run
```
cargo make
```
### result
grpc 0.2.1 compile failed
### solution
It is because grpc v0.2.1 does not strictly specify its dependency.
I edited its dependency locally: 
* futures from 0.* to 0.1.*
* tokio from 0.* to 0.1.*
* tls-api from 0.* to 0.1

## Obtaining contract MRENCLAVE
### status
cargo make is done
### run
```
python scripts/parse_enclave.py target/enclave/token.signed.so
```
### result
contracts are not built to *.signed.so
### run
```
cd contracts/key-manager/ && cargo make
```
### result
```
[cargo-make] INFO - cargo-make 0.10.4
[cargo-make] INFO - Using Build File: Makefile.toml
[cargo-make] INFO - Task: default
[cargo-make] INFO - External file not found, skipping.
[cargo-make] INFO - Setting Up Env.
[cargo-make] INFO - Running Task: init
[cargo-make] INFO - Running Task: pre-format
[cargo-make] INFO - Running Task: format-stable
[cargo-make] INFO - Running Task: format-nightly
[cargo-make] INFO - Execute Command: "cargo" "fmt" "--" "--write-mode=overwrite"
`cargo manifest` failed.
usage: cargo fmt [options]
```
Actually Makefile.toml has extends="../Makefile.toml" but there is no Makefile.toml in "contract" directory.  
I use compiled enclaves from earlier version ekiden and pass this procedure. Simply copy them into directory target/enclaves

### read token.signed.so
run
```
python scripts/parse_enclave.py target/enclave/token.signed.so

```
result
```
...
# ECALLs table found at 0xca3cb2f7
Traceback (most recent call last):
  File "scripts/parse_enclave.py", line 490, in <module>
    necalls, = unpack("<I", p.blob[epos:epos+4])
struct.error: unpack requires a string argument of length 4
```


## run consensus node
### status
cargo make is done
### run
```
bash scripts/sgx-enter.sh
cargo run -p consensus (in path /code)
```
### result
```
error: package `consensus` is not a member of the workspace
```
I am confused that Cargo.toml is in the path which defines workspace.  
Use ```cd consensus && cargo run``` to skip this.  

Then
```
Compiling ekiden-consensus v0.1.0-alpha.1 (file:///code/consensus)
    Finished dev [unoptimized + debuginfo] target(s) in 6.57 secs
     Running `/code/target/debug/ekiden-consensus`
Ekiden Consensus Node starting on port 9002 ... 
thread 'main' panicked at 'called `Result::unwrap()` on an `Err` value: Http(Other("addr is resolved to more than one addr"))', libcore/result.rs:945:5
note: Run with `RUST_BACKTRACE=1` for a backtrace.
```
It seems something goes wrong when unwrap address (default localhost).  
I change default address from "localhost" to "127.0.0.1" and problem solved. I wonder whether this only happens on me?  
```
        .arg(
            Arg::with_name("tendermint-host")
                .long("tendermint-host")
                .takes_value(true)
                .default_value("localhost"), # to 127.0.0.1
        )
```
Similar situation happens when passing "localhost" as default address...I change them all.
### to start tendermint run
```
bash ./scripts/tendermint-start.sh
```
It is successful only when the container name is "ekiden". Otherwise should manully edit the script.

## run compute node
### status
consensus is running
tendermint is running
### run:
```
export IAS_PKCS="/code/client.pfx"
scripts/run_contract.sh token
```
### result
```
WARNING: IAS is not configured, validation will always return an error.
Compute node listening at 9001
thread '<unnamed>' panicked at 'EnclaveIdentity::identity_init: Error { message: "identity_create: SGX_ERROR_OUT_OF_MEMORY" }', libcore/result.rs:945:5
note: Some details are omitted, run with `RUST_BACKTRACE=full` for a verbose backtrace.
stack backtrace:
   0: std::sys::unix::backtrace::tracing::imp::unwind_backtrace
             at libstd/sys/unix/backtrace/tracing/gcc_s.rs:49
   1: std::sys_common::backtrace::_print
             at libstd/sys_common/backtrace.rs:71
   2: std::panicking::default_hook::{{closure}}
             at libstd/sys_common/backtrace.rs:59
             at libstd/panicking.rs:380
   3: std::panicking::default_hook
             at libstd/panicking.rs:396
   4: std::panicking::rust_panic_with_hook
             at libstd/panicking.rs:576
   5: std::panicking::begin_panic
             at libstd/panicking.rs:537
   6: std::panicking::begin_panic_fmt
             at libstd/panicking.rs:521
   7: rust_begin_unwind
             at libstd/panicking.rs:497
   8: core::panicking::panic_fmt
             at libcore/panicking.rs:71
   9: core::result::unwrap_failed
             at /checkout/src/libcore/macros.rs:23
  10: <core::result::Result<T, E>>::expect
             at /checkout/src/libcore/result.rs:809
  11: ekiden_compute::server::ComputeServerWorker::create_contract
             at compute/src/server.rs:120
  12: ekiden_compute::server::ComputeServerWorker::new
             at compute/src/server.rs:83
  13: ekiden_compute::server::ComputeServerImpl::new::{{closure}}
             at compute/src/server.rs:414
```
compute node is still listening but cannot respond any client.
