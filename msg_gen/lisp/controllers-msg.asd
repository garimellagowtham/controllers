
(cl:in-package :asdf)

(defsystem "controllers-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "ctrl_command" :depends-on ("_package_ctrl_command"))
    (:file "_package_ctrl_command" :depends-on ("_package"))
  ))