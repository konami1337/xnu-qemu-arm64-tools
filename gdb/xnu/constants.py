"""
Here defined all constants, serving all mudules.
"""

from enum import Enum

GLOBAL_THREADS_PTR = 0xfffffff00760f9e0
GLOBAL_TASKS_PTR = 0xfffffff00760f9c0
NULL_PTR = 0x0000000000000000
NULL_PTR_STR = "0x0000000000000000"
CURRENT_THREAD = "$TPIDR_EL1"

IE_BITS_TYPE_MASK = 0x001f0000

IO_BITS_KOTYPE = 0x00000fff


class NextPcHelpOffsets(Enum):
    """ Info taken by reversing the 16B92 kernel version """
    NEXT_IN_THREAD_RUN = 0xfffffff0070e7d0c
    NEXT_IN_THREAD_BLOCK = 0xfffffff0070e3554
    EXEPTION_RETURN_PTR = 0xfffffff0070a1800
    SP_OFFSET_FROM_KRN_STACK = 0x100
    THREAD_INVOKE_FRAME_SIZE = 0x90
    X21_IN_THREAD_INVOKE_FRAME = 0x28
    STORED_LR_IN_THREAD_INVOKE_FRAME = 0x88


class ThrdItrType(Enum):
    """ Info taken by reversing the 16B92 kernel version """
    GLOBAL = 0
    TASK = 1


class ThreadOffsets(Enum):
    """
    What had been parsed of thread struct
    xnu kernel ref: darwin-xnu/osfmk/kern/thread.h (thread)
    """
    CONTINUATION = 0x80
    CURRENT_STATE = 0xa0
    THREAD_ID = 0x3e0
    GLOBAL_THREADS = 0x348
    TASK_THREADS = 0x358
    TASK = 0x368
    CONTEXT_USER_DATA_PTR = 0x430
    KSTACK_PTR = 0x448
    VOUCHER_PTR = 0x510
    VOUCHER_NAME = 0x50C


class TaskOffsets(Enum):
    """
    What had been parsed of task struct
    xnu kernel ref: darwin-xnu/osfmk/kern/task.h (task)
    """
    TASK_NEXT = 0x28
    THREAD_LST_FROM_TASK = 0x40
    ITK_SELF = 0xD8
    ITK_NSELF = 0xE0
    ITK_SSELF = 0xE8
    BSD_INFO = 0x358
    IPC_SPACE = 0x300


class BSDInfoOffsets(Enum):
    """ xnu kernel ref: darwin-xnu/bsd/sys/proc_internal.h (proc) """
    PID_IN_BSD_INFO = 0x60
    NAME_INBSD_INFO = 0x261


class IPCSpaceOffsets(Enum):
    """ xnu kernel ref: darwin-xnu/osfmk/ipc/ipc_space.h (ipc_space) """
    IS_TABLE_SIZE = 0x14
    IS_TABLE_FREE = 0x18
    IS_TABLE = 0x20
    IS_LOW_MOD = 0x38
    IS_HIGH_MOD = 0x3C


class IPCEntryOffsets(Enum):
    """ xnu kernel ref: darwin-xnu/osfmk/ipc/ipc_entry.h (ipc_entry) """
    IE_BITS = 0x08
    IE_INDEX = 0x0C
    INDEX = 0x10


class IPCObjectOffsets(Enum):
    """ xnu kernel ref: darwin-xnu/osfmk/ipc/ipc_object.h (ipc_object) """
    IO_REFS = 0x04
    IO_LOCK_DATA = 0x08
    IP_MSG = 0x24


class IPCPortOffsets(Enum):
    """ xnu kernel ref: darwin-xnu/osfmk/ipc/ipc_port.h (ipc_port) """
    IP_MSG = 0x18
    DATA = 0x60
    KDATA = 0x68
    IP_NSREQ = 0x70
    IP_PDREQ = 0x78
    IP_REQ = 0x80
    KDATA2 = 0x88
    IP_CTXT = 0x90
    IP_SPREQ = 0x98  # bitmap
    IP_MSCNT = 0x9C
    IP_SRIGHTS = 0xA0
    IP_SORIGHTS = 0xA4


# osfmk/kern/ipc_kobject.h
IO_BITS_TYPES = [
    "IKOT_NONE",
    "IKOT_THREAD",
    "IKOT_TASK",
    "IKOT_HOST",
    "IKOT_HOST_PRIV",
    "IKOT_PROCESSOR",
    "IKOT_PSET",
    "IKOT_PSET_NAME",
    "IKOT_TIMER",
    "IKOT_PAGING_REQUEST",
    "IKOT_MIG",
    "IKOT_MEMORY_OBJECT",
    "IKOT_XMM_PAGER",
    "IKOT_XMM_KERNEL",
    "IKOT_XMM_REPLY",
    "IKOT_UND_REPLY",
    "IKOT_HOST_NOTIFY",
    "IKOT_HOST_SECURITY",
    "IKOT_LEDGER",
    "IKOT_MASTER_DEVICE",
    "IKOT_TASK_NAME",
    "IKOT_SUBSYSTEM",
    "IKOT_IO_DONE_QUEUE",
    "IKOT_SEMAPHORE",
    "IKOT_LOCK_SET",
    "IKOT_CLOCK",
    "IKOT_CLOCK_CTRL",
    "IKOT_IOKIT_IDENT",
    "IKOT_NAMED_ENTRY",
    "IKOT_IOKIT_CONNECT",
    "IKOT_IOKIT_OBJECT",
    "IKOT_UPL",
    "IKOT_MEM_OBJ_CONTROL",
    "IKOT_AU_SESSIONPORT",
    "IKOT_FILEPORT",
    "IKOT_LABELH",
    "IKOT_TASK_RESUME",
    "IKOT_VOUCHER",
    "IKOT_VOUCHER_ATTR_CONTROL",
    "IKOT_WORK_INTERVAL",
    "IKOT_UX_HANDLER"
]
