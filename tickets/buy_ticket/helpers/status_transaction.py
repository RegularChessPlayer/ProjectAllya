from enum import Enum


class StatusTransaction(Enum):

    APC = 'authorized_pending_capture'
    PD = 'paid'
    NA = 'not_authorized'
    CA = 'captured'
    PC = 'partial_capture'
    WCP = 'waiting_capture'
    RE = 'refunded'
    VO = 'voided'
    PR = 'partial_refunded'
    PV = 'partial_void'
    EOV = 'error_on_voiding'
    EOR = 'error_on_refunding'
    WCN = 'waiting_cancellation'
    WE = 'with_error'
    FA = 'failed'

